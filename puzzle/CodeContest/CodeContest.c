#include <stdio.h>

#define N 2000
#define MAX_SIZE 1000000000

int main(){
	int num_piece;
	int pieces_sizes[N];
	int i, j;
	int max_benefit = 0;
	int benefit_temp = 0;

	// initialize
	for(i = 0; i < N; i++){
		pieces_sizes[i] = 0;
	}
	
	printf("input number of piece of cake >>");
	scanf("%d", &num_piece);
	
	printf("tell me each size of piece of the cake\n");
	for(i = 0; i < num_piece; i++){
		printf(">> ");
		scanf("%d", &pieces_sizes[i]);
	}
	
	printf("each size of the piece of the cake is: [ ");
	for(i = 0; i < num_piece; i++) printf("%d ", pieces_sizes[i]);
	printf("]\n");
	
	// estimate max benefit
	for(i = 0; i < num_piece; i++){
		printf("target: [");
		for(j = 0; j < num_piece; j++) printf("%d ", pieces_sizes[j]);
		printf("]\n");
		benefit_temp = estimateBenefit(pieces_sizes);
		printf("you earned: %d\n", benefit_temp);
		if(benefit_temp > max_benefit){
			max_benefit = benefit_temp;
		}
	}
	
	return 0;
}

int estimateBenefit(int pieces[]){

	return 0;	// max();
}

