//https://www.hackerrank.com/contests/w31/challenges/beautiful-word

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

const char vowels[]= {'a', 'e', 'i','o', 'u', 'y'};

int isvowel(char c) {    
    static int nvowels = 6;
    for(int i=0; i < nvowels; ++i) {
        if(c==vowels[i]) {
            return 1;
        }
    }
    return 0;
}

int main(){
    char* w = (char *)malloc(512000 * sizeof(char));
    
    scanf("%s",w);
    int len_ = strlen(w);
    
    int already_printed=0;
    for(int i=0; i < (len_-1); ++i) {
        if(w[i]==w[i+1]) {
            printf("No");
            already_printed=1;
            break;
        }
        if(isvowel(w[i])&&isvowel(w[i+1])) {
            printf("No");
            already_printed=1;
            break;
        }
    }
    if(!already_printed) {
        printf("Yes");
    }
    // Print 'Yes' if the word is beautiful or 'No' if it is not.
    return 0;
}
