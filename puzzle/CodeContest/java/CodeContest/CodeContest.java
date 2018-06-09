import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

class CodeContest{
	public static void main(String[] args){
		System.out.print("input number of piece of cake >> ");
		Scanner scanner = new Scanner(System.in);
		int num_piece = scanner.nextInt();
		
		System.out.println("tell me each size of piece of the cake");
		ArrayList<Integer> pieces_sizes = new ArrayList<Integer>();
		for(int i = 0; i < num_piece; i++){
			System.out.print(">> ");
			pieces_sizes.add(scanner.nextInt());
		}
		System.out.println("each size of the piece of the cake is: " + pieces_sizes);

		int max_benefit = 0;
		for(int i = 0; i < pieces_sizes.size(); i++){
			System.out.println("target: " + pieces_sizes);
			int benefit_temp = estimateBenefit(pieces_sizes);
			System.out.println("you earned " + benefit_temp);
			if(benefit_temp >= max_benefit){
				max_benefit = benefit_temp;
			}
			// shift
			Collections.rotate(pieces_sizes, 1);
		}

		System.out.println("You can take at most " + max_benefit);
	}


	static int estimateBenefit(ArrayList<Integer> pieces){
		ArrayList<Integer> pieces_x_takes_head = new ArrayList<Integer>(pieces);
		ArrayList<Integer> pieces_x_takes_tail = new ArrayList<Integer>(pieces);
		int benefit_head = 0;
		int benefit_tail = 0;
		
		if(pieces.size() >= 1){
			benefit_head += pieces_x_takes_head.remove(0);
			benefit_tail += pieces_x_takes_tail.remove(pieces.size() - 1);
		}

		if(pieces.size() >= 2){
			if(pieces_x_takes_head.get(0) > pieces_x_takes_head.get(pieces_x_takes_head.size() - 1)){
				pieces_x_takes_head.remove(0);
			}else{
				pieces_x_takes_head.remove(pieces_x_takes_head.size() - 1);
			}

			if(pieces_x_takes_tail.get(0) > pieces_x_takes_tail.get(pieces_x_takes_tail.size() - 1)){
				pieces_x_takes_tail.remove(0);
			}else{
				pieces_x_takes_tail.remove(pieces_x_takes_tail.size() - 1);
			}

			benefit_head += estimateBenefit(pieces_x_takes_head);
			benefit_tail += estimateBenefit(pieces_x_takes_tail);
		}
		
		return Math.max(benefit_head, benefit_tail);
	}

}
