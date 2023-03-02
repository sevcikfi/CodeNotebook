---
alias:
tag: meta
---

# Seyfor & ComAp - SW analytik & Junior dev task

## Task

```VBA
Skriptování

Níže je pseudoscript, který má výstupovou hodnotu bool.
Pseudoskript se váže k příchozí XML zprávě (=Message) a na skupinu/element.

- Vytvořte slovní zadání pro tento skript
- Popište slovy kdy bude výstup false


Result = true
IF Message.CustomsOfficeOfDestination.Exists(TRUE) THEN
    IF NOT CodeLists.CustomsOfficeOfDestination.Exists(Current.Identification = Message.CustomsOfficeOfDestination.Identification) THEN
        Result = false
    ENDIF
ELSE
    IF Message.CustomsOfficeOfTransit.Exists(TRUE) THEN
        IF NOT CodeLists.CustomsOfficeOfTransit.Exists(Current.Identification = Message.CustomsOfficeOfDestination.Identification) THEN
            Result = false
        ENDIF
    ELSE
        IF Message.CustomsOfficeOfExitForTransit.Exists(TRUE) THEN
            IF NOT CodeLists.CustomsOfficeOfExitForTransit.Exists(Current.Identification = Message. CustomsOfficeOfExitForTransit.Identification) THEN
                Result = false
            ENDIF
        ENDIF
    ENDIF
ENDIF
```

## Solution

### What might have been *text instructions*

"Write script which will by default evaluate true unless `Customs Office Of Destination`'s, `Customs Office Of Transit`'s or `Customs Office Of Exit For Transit`'s identification isn't on one of appropriate list of codes."

### The code will result in false evaluation in 3 instances

1. When the `CustomsOfficeOfDestination` field exists on the Message but `CustomsOfficeOfDestination.Identification` is not in `CodeLists.CustomsOfficeOfDestination`.
2. If `CustomsOfficeOfTransit` exists on the Message instead of the previous but `CodeLists.CustomsOfficeOfTransit` does not contain `CustomsOfficeOfDestination.Identification`.
3. If `CustomsOfficeOfExitForTransit.Exists` exists on the Message instead of former two but `CustomsOfficeOfExitForTransit.Identification` is not in `CodeLists.CustomsOfficeOfExitForTransit`.
