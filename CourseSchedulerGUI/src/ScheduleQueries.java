
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;


/**
 *
 * @author tarunravikumar
 */
public class ScheduleQueries {
    private static Connection connection;
    private static ArrayList<String> faculty = new ArrayList<String>();
    private static PreparedStatement addSchedule;
    private static PreparedStatement getScheduleList;
    private static PreparedStatement getScheduledStudentCount;   
    private static PreparedStatement getScheduleByStudent;   
    private static ResultSet resultSet;
    
    public static void addScheduleEntry(ScheduleEntry name)  {
        connection = DBConnection.getConnection();
        try{
            addSchedule = connection.prepareStatement("insert into app.schedule (Semester, courseCode, StudentID, Status, Timestamp) values (?,?,?,?,?)");
            addSchedule.setString(1, name.getSemester());
            addSchedule.setString(2, name.getCourseCode());
            addSchedule.setString(3, name.getStudentID());
            addSchedule.setString(4, name.getStatus());
            addSchedule.setTimestamp(5, name.getTimestamp());
            addSchedule.executeUpdate();
        }
        catch(SQLException sqlException){
            sqlException.printStackTrace();
        }
    }
    
    public static ArrayList<ScheduleEntry> getScheduleByStudent(String semester, String studentID) {
        connection = DBConnection.getConnection();
        ArrayList<ScheduleEntry> studentSchedule = new ArrayList<ScheduleEntry>();
        try
        {
            getScheduleByStudent = connection.prepareStatement("select Semester, courseCode, StudentID, Status, Timestamp from app.schedule where semester=? and studentID=?");
            getScheduleByStudent.setString(1, semester);
            getScheduleByStudent.setString(2, studentID);
            resultSet = getScheduleByStudent.executeQuery();
            
            while(resultSet.next())
            {
                ScheduleEntry load=new ScheduleEntry(resultSet.getString(1), resultSet.getString(2), resultSet.getString(3), resultSet.getString(4), resultSet.getTimestamp(5));
                studentSchedule.add(load);
            }
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
        return studentSchedule;        
    }
    
    public static int getScheduledStudentCount(String currentSemester, String courseCode){
        connection = DBConnection.getConnection();
        int counter=0;
        
        try
        {
            getScheduledStudentCount = connection.prepareStatement("select count(studentID) from app.schedule where semester = ? and courseCode = ?");
            getScheduledStudentCount.setString(1, currentSemester);
            getScheduledStudentCount.setString(2, courseCode);
            resultSet = getScheduledStudentCount.executeQuery();
            
            while(resultSet.next()){
                counter = resultSet.getInt(1);
            }
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
        return counter;        
    }

    
}
