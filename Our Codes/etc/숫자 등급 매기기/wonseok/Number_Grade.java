import java.util.Scanner;

public class Number_Grade {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		
		int n, m;
		int UR = 0;
		int SR = 0;
		int R = 0;
		int nomal = 0;
		
		n = input.nextInt();
		m = input.nextInt();
		
		int[] arr = new int[m+1];
		
		for(int i = 0; i <= m; i++) {
			arr[i] = input.nextInt();
		} // m���� �������� �Է�
		
		for(int i = 1; i <= n; i++) {
			if((i == 1) || ((i & (i-1)) == 0 ) || (i % arr[0]==0 && i % arr[1] == 0 && i % arr[2] == 0)) {
				UR++;
			// 2�� �ŵ������� �������� ǥ���ϸ� 10, 100, 1000 ���� ǥ���ǰ� 
			// 2�� �ŵ����� - 1 �� ��������  01, 011, 011 ���� ǥ���Ǿ� ���� & ������ �ϸ� 0�� ��ȯ�ȴ�.
			}else if((i%arr[0]==0 && i%arr[1]==0 && i% arr[2] !=0) || 
					 (i%arr[0]==0 && i%arr[1]!=0 && i% arr[2] ==0) ||
					 (i%arr[0]!=0 && i%arr[1]==0 && i% arr[2] ==0)) {
				SR++;
			}else if(i%arr[0]==0 ^ i%arr[1]==0 ^ i% arr[2] ==0) { // true true true�� ���� �տ��� �� ���Ա� ������ xor������ ��밡���ϴ�.
				R++;
			}else {
				nomal++;
			}		
		}
		
		System.out.printf("UR: %d SR: %d R: %d N: %d", UR, SR, R, nomal);
		
	}

}
