package BD;

import com.mysql.cj.jdbc.NonRegisteringDriver;

import java.sql.Connection;
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBUtils {
    private static final String dbURL = "jdbc:mysql://localhost:3306/mysql?allowPublicKeyRetrieval=true&useSSL=false&serverTimezone=Europe/Moscow";
    private static final String dbUsername = "BigBiza";
    private static final String dbPassword = "Sonik2013";
    public static Connection getConnection() {

        Connection connection = null;
        try {
            Driver driver = new NonRegisteringDriver();
            DriverManager.registerDriver(driver);
            connection = DriverManager.getConnection(dbURL, dbUsername, dbPassword);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return connection;
    }
}