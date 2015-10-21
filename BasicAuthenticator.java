
import java.net.Authenticator;
import java.net.PasswordAuthentication;

public class BasicAuthenticator extends Authenticator {
        String baName;
        String baPassword;
        public BasicAuthenticator(String baName1, String baPassword1) {
            baName = baName1;
            baPassword = baPassword1;
        }
        @Override
            public PasswordAuthentication getPasswordAuthentication() {
                System.out.println("Authenticating...");
                return new PasswordAuthentication(baName, baPassword.toCharArray());
            }
    }; 