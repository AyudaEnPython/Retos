/** AyudaEnPython: https://www.facebook.com/groups/ayudapython
 * 
 *    Estatus    : AC 
 *    Porcentaje : 100.00%
 *    Memoria    : 1112 KiB
 *    Tiempo     : 0.02s
*/
#include <stdio.h>
#include <float.h>

int main() {
    float e, l, t;
    float v = 0;
    while (1) {
        scanf("%g %g %g", &e, &l, &t);
        if (e == 0 && l == 0 && t == 0) 
            return 0;
        if (e <= 0 || l <= 0 || t <= 0)
            printf("ERROR\n");
        else {
            e /= 1000;
            t /= 3600;
            v = e / t;
            if (v < l)
                printf("OK\n");
            else
                if (v < l * 1.2)
                    printf("MULTA\n");
                else
                    printf("PUNTOS\n");
        }
    }
    return 0;
}
