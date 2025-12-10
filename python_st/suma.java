import java.util.*;
class main{
    public static void main(String[] args) {
        Scanner ob=new Scanner(System.in);
        int total_bank_balance=20000;
        int temp;
        int user_withdra_amount=ob.nextInt();
        while(500<total_bank_balance){
            if(total_bank_balance>500){
                temp=user_withdra_amount-total_bank_balance;
                System.out.println(user_withdra_amount);
                System.out.print("remamount:"+temp);
            }
        }
    }
}