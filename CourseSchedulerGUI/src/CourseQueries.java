
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;


/**
 *
 * @author tarunravikumar
 */
public class CourseQueries {
    private static Connection connection;
    private static ArrayList<String> faculty = new ArrayList<String>();
    private static PreparedStatement addCourse;
    private static PreparedStatement getCourses;
    private static ResultSet resultSet;
    
    
    public static ArrayList<CourseEntry> getAllCourses(String semester) {
        connection = DBConnection.getConnection();
        ArrayList<CourseEntry> courses = new ArrayList<CourseEntry>();
        try {
            getCourses = connection.prepareStatement("select Semester, CourseCode, Description, Seats from app.course where semester=?");
            getCourses.setString(1, semester);
            resultSet = getCourses.executeQuery();

            while (resultSet.next()) {
                CourseEntry newObj = new CourseEntry(resultSet.getString(1), resultSet.getString(2), resultSet.getString(3), resultSet.getInt(4));
                courses.add(newObj);
            }
        } 
        catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }
        return courses;
    }
    
    public static void addCourse(CourseEntry course)
    {
        connection = DBConnection.getConnection();
        try
        {
            addCourse = connection.prepareStatement("insert into app.course (Semester, CourseCode, Description, Seats) values (?,?,?,?)");
            addCourse.setString(1, course.getSemester());
            addCourse.setString(2, course.getCourseCode());
            addCourse.setString(3, course.getDescription());
            addCourse.setInt(4, (course.getSeats()));
            
            addCourse.executeUpdate();
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
        
    }
    
    
    public static ArrayList<String> getAllCourseCodes(String semester){
        connection = DBConnection.getConnection();
        ArrayList<String> courseCode = new ArrayList<String>();
        try
        {
            getCourses = connection.prepareStatement("select courseCode from app.course");
            resultSet = getCourses.executeQuery();
            
            while(resultSet.next())
            {
                courseCode.add(resultSet.getString(1));
            }
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
        return courseCode;
    
    
    }
    
    public static int getCourseSeats(String semester, String courseCode){
        
        connection = DBConnection.getConnection();
        int numSeat = 0;
        try
        {
            getCourses = connection.prepareStatement("select seats from app.course where semester=? and courseCode=?");
            getCourses.setString(1, semester);
            getCourses.setString(2, courseCode);
            resultSet = getCourses.executeQuery();
            
            while(resultSet.next())
            {
                numSeat=Integer.parseInt(resultSet.getString(1));
            }
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
        return numSeat;
    
    
    }
}
