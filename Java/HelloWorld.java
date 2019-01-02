public class HelloWorld{
    public static void main(String[] args){
        for(int i=0; i<args.length; i++)
          pl("\033[31mVocê digitou: "+args[i]);
        pl("\033[mFim do Programa!");
    }

    private static void pl(Object s){
      System.out.println(s);
    }
}