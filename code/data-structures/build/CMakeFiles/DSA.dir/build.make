# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/martinrodriguez/Research/interview-study-guide/code/data-structures

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/martinrodriguez/Research/interview-study-guide/code/data-structures/build

# Include any dependencies generated for this target.
include CMakeFiles/DSA.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/DSA.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/DSA.dir/flags.make

CMakeFiles/DSA.dir/impl/main.o: CMakeFiles/DSA.dir/flags.make
CMakeFiles/DSA.dir/impl/main.o: ../impl/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/martinrodriguez/Research/interview-study-guide/code/data-structures/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/DSA.dir/impl/main.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/DSA.dir/impl/main.o -c /home/martinrodriguez/Research/interview-study-guide/code/data-structures/impl/main.cpp

CMakeFiles/DSA.dir/impl/main.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/DSA.dir/impl/main.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/martinrodriguez/Research/interview-study-guide/code/data-structures/impl/main.cpp > CMakeFiles/DSA.dir/impl/main.i

CMakeFiles/DSA.dir/impl/main.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/DSA.dir/impl/main.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/martinrodriguez/Research/interview-study-guide/code/data-structures/impl/main.cpp -o CMakeFiles/DSA.dir/impl/main.s

# Object files for target DSA
DSA_OBJECTS = \
"CMakeFiles/DSA.dir/impl/main.o"

# External object files for target DSA
DSA_EXTERNAL_OBJECTS =

DSA: CMakeFiles/DSA.dir/impl/main.o
DSA: CMakeFiles/DSA.dir/build.make
DSA: CMakeFiles/DSA.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/martinrodriguez/Research/interview-study-guide/code/data-structures/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable DSA"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/DSA.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/DSA.dir/build: DSA

.PHONY : CMakeFiles/DSA.dir/build

CMakeFiles/DSA.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/DSA.dir/cmake_clean.cmake
.PHONY : CMakeFiles/DSA.dir/clean

CMakeFiles/DSA.dir/depend:
	cd /home/martinrodriguez/Research/interview-study-guide/code/data-structures/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/martinrodriguez/Research/interview-study-guide/code/data-structures /home/martinrodriguez/Research/interview-study-guide/code/data-structures /home/martinrodriguez/Research/interview-study-guide/code/data-structures/build /home/martinrodriguez/Research/interview-study-guide/code/data-structures/build /home/martinrodriguez/Research/interview-study-guide/code/data-structures/build/CMakeFiles/DSA.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/DSA.dir/depend

