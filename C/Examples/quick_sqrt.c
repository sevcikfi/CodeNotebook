#include <stdio.h>

/// @brief Stolen from Microchip something
/// @param Value 
/// @return 
unsigned SquareRoot( unsigned Value )
       {
         unsigned Root = 0;
         unsigned Bit;
         for ( Bit = 0x4000; Bit > 0; Bit >>= 2 )
           {
             unsigned Trial = Root + Bit;
             Root >>= 1;
             if ( Trial <= Value )
               {
                 Root += Bit;
                 Value -= Trial;
               }
           }
         return Root;
       }
     

/// @brief from Quake III Arena
/// @param number 
/// @return 
float Q_rsqrt( float number )
{
	long i;
	float x2, y;
	const float threehalfs = 1.5F;

	x2 = number * 0.5F;
	y  = number;
	i  = * ( long * ) &y;                       // evil floating point bit level hacking
	i  = 0x5f3759df - ( i >> 1 );               // what the fuck? 
	y  = * ( float * ) &i;
	y  = y * ( threehalfs - ( x2 * y * y ) );   // 1st iteration
//	y  = y * ( threehalfs - ( x2 * y * y ) );   // 2nd iteration, this can be removed

	return y;
}

#include <stdint.h> // uint32_t
//no more undefined? xd	
float Q_rsqrt(float number)
{
	union {
		float    f;
		uint32_t i;
	} conv = { .f = number };
	conv.i  = 0x5f3759df - (conv.i >> 1);
	conv.f *= 1.5F - (number * 0.5F * conv.f * conv.f);
	return conv.f;
}

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}
