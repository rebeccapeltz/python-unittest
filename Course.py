import json

class Course:
    """
    A class representing course data.

    Properties:
    - Course Name (str): The name of the couse
    - Credits (int): The number of credits to be earned in the course
    """
    FILE_NAME="courses.json"

    def __init__(self, course_name: str = "", course_credits: int = 0):
        self.course_name = course_name
        self.course_credits = course_credits

    @property
    def course_name(self):
        return self.__course_name.title()

    @course_name.setter
    def course_name(self, value: int):
        if value is not None:
            self.__course_name = value
        else:
            raise ValueError("The course name should not be empty")

    @property
    def course_credits(self):
        return self.__course_credits

    @course_credits.setter
    def course_credits(self, value: int):
        if (type(value) == int) and (value >= 0 and value <= 5):
            self.__course_credits = value
        else:
            raise ValueError("Course credits input should be an integer between 0 and 5 inclusive.")

    def __str__(self):
        return f"{self.course_name},{self.course_credits}"

    def print_course_info(self):
        print(f"{self.course_name} awards {self.course_credits}")

    def print_course_info_expanded(self):
        print(f"Course Name: {self.course_name}")
        print(f"Course Credits: {self.course_credits}")

    @staticmethod
    def convert_course_to_json(course):
        return [{"course_name":course.course_name,"course_credits":course.course_credits}]

    @staticmethod
    def convert_dict_to_course(course_dict):
        course_name = course_dict["course_name"]
        course_credits = course_dict["course_credits"]
        course = Course(course_name,course_credits)
        return course

    @staticmethod
    def convert_json_to_courses(json_data):
        courses = []
        for course_dict in json_data:
            course = Course.convert_dict_to_course(course_dict)
            courses.append(course)
        return courses

    @staticmethod
    def convert_course_to_dict(course):
        return {"course_name":course.course_name,"course_credits":course.course_credits}

    @staticmethod
    def convert_courses_to_json(courses):
        json_data = []
        for course in courses:
            json_data.append((Course.convert_course_to_dict(course)))
        return json_data;



    @staticmethod
    def write_courses_to_file(FILE_NAME,courses):
        pass

    @staticmethod
    def read_courses_from_file(file_name):
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
        except FileNotFoundError:
            raise FileNotFoundError("Text file must exist before running this script!")
        except Exception:
            raise Exception("There was a non-specific error!")
        return list_of_dictionary_data

    def read_course_data_from_file(file_name: str):
        """ This function reads data from a json file and loads it into a list of dictionary rows
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
        except FileNotFoundError:
            raise FileNotFoundError("Text file must exist before running this script!")
        except Exception:
            raise Exception("There was a non-specific error!")
        return list_of_dictionary_data

    @staticmethod
    def write_course_data_to_file( course_json_data: list,file_name: str):
        """ This function writes data to a json file with data from a list of dictionary rows
        """
        try:
            with open(file_name, "w") as file:
                json.dump(course_json_data, file)
        except TypeError:
            raise TypeError("Please check that the data is a valid JSON format")
        except PermissionError:
            raise PermissionError("Please check the data file's read/write permission")
        except Exception as e:
            raise Exception("There was a non-specific error!")


