public class patterns {
    public static void main(String[] args) {
        System.out.println("1st Pattern: ");
        for (int i =0; i<4;i++) {
            System.out.println("");
            for(int j =0;j<5;j++ ){
                System.out.print("*");
            }
        }

        System.out.println("\n2nd pattern:\n");
        int n = 4;
        int m = 5;


        for (int i = 1; i<=n; i++){
            for  (int j= 1; j<=m;j++){
                if (i==1 || j==1 || i==n || j==m) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
     
    System.out.println("\n 3rd patter: \n ");
    int l = 4;
    for (int i =  1; i <=n; i++) {
        for (int j=1; j<=i;j++){
            System.out.print("*");
        }
        System.out.println();
    }
    
    System.out.println("4th pattern:");
    
    for( int i =4; i>=1; i--) {
        for (int j =1; j<=i; j++) {
            System.out.print("*");
        } 
        System.out.println();
    }

    System.out.println("\n 5th pattern : \n ");
    int p =4;
    for (int i =1; i<=p; i++){
        for (int j =1;j<=p-i; j++) {
            System.out.print(" ");
        }for (int j = 1 ; j<=i; j++) {
            System.out.print("*");
         }
        System.out.println();
        
        }
    

        System.out.println("\n6th pattern\n");

        for(int i = 1; i<=5; i++) {
            for (int j =1; j<=i; j++) {
                System.out.print(j + " ");
            }
            System.out.println();
        } 


        System.out.println("\n7th pattern\n");

        for(int i = 5; i>=1; i--) {
            for (int j =1; j<=i; j++) {
                System.out.print(j + " ");
            }
            System.out.println();
        } 

        System.out.println("\n8th pattern\n");
        // floyds traingle 
        int h= 5;
        int number =1;
        for (int i =1; i<=h; i++) {
            for (int j = 1; j<=i; j++ ) {
                System.out.print(number+ " ");
                number  = number +1 ;
            }
            System.out.println();
        }

        System.out.println("\n9th pattern\n");
        int g = 5;
        for (int i =1; i<=5; i++) {
            for (int j =1; j<=i; j++) {
                int sum = i+j;
                if(sum%2==0) {
                    System.out.print("1 ");

                }else {System.out.print("0 ");}
            }
            System.out.println();
        }





    }
    
}



