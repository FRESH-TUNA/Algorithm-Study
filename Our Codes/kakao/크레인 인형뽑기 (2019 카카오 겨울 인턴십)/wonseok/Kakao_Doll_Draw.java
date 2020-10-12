import java.util.Stack;

public class Kakao_Doll_Draw {

	public static void main(String[] args) {
		int board[][] = {{0,0,0,0,0},
						 {0,0,1,0,3},
						 {0,2,5,0,1},
						 {4,2,4,4,2},
						 {3,5,1,3,1}};
		int move[] = {1, 5, 3, 5, 1, 2, 1, 4};
		System.out.println(solution(board, move));
	}
	
	public static int solution(int[][] board, int[] moves) {
		int answer =0;
		Stack<Integer> basket = new Stack<>();
		for(int i = 0; i < moves.length; i++) {
			for(int j = 0; j < board.length; j++) {
				if(board[j][moves[i]-1] != 0) {
					if((basket.empty()==false) && basket.peek()==board[j][moves[i]-1]) {  // ���� ���ε��� ���� ���� ���� ���̶� ���� ���
						basket.pop();								   // �������� ���� �����ϰ�
						answer += 2;							 		   // answer��  2�� ���Ѵ�.(������ 2���� ������� ������)
						board[j][moves[i]-1] = 0; 			 		   // ������ �̾ƿ� �ڸ��� 0���� �ٲ۴�.,	
						break;
					}else {
						basket.push(board[j][moves[i]-1]);	 		   // �������� ���� �ٸ��� ���簪�� push�Ѵ�.
						board[j][moves[i]-1] = 0;				 		   //	�׸��� �̾ƿ� �ڸ��� 0���� �ٲ۴�.
						break;
					}
				}else {
					continue;										   // 0�̸� �ǳʶڴ�.
				}
			}
		}
		return answer;
	}
}


