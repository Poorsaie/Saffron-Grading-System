% Define saffron grades
grade(high, good).
grade(medium, medium).
grade(low, low).

% Grading rules based on color
grade_color(red, good).
grade_color(yellow, medium).
grade_color(white, low).

% Grading rules based on size
grade_size(big, good).
grade_size(medium, medium).
grade_size(small, low).

% Grading rules based on shape
grade_shape(straight, high).
grade_shape(curved, medium).
grade_shape(broken, low).

% Grading rules based on thickness
grade_thickness(thick, high).
grade_thickness(medium, medium).
grade_thickness(thin, low).

% Classify saffron based on color, size, shape, and thickness
classify_saffron(Color, Size, Shape, Thickness, Grade) :-
    grade_color(Color, ColorGrade),
    grade_size(Size, SizeGrade),
    grade_shape(Shape, ShapeGrade),
    grade_thickness(Thickness, ThicknessGrade),
    combine_grades(ColorGrade, SizeGrade, ShapeGrade, ThicknessGrade, Grade).

% Combine color, size, shape, and thickness grades
combine_grades(good, good, _, _, high).
combine_grades(medium, medium, good, _, high).
combine_grades(medium, medium, medium, good, high).
combine_grades(medium, medium, low, _, medium).
combine_grades(low, low, _, _, medium).
combine_grades(_, _, _, _, low).
combine_grades(_, _, _, _, unknown).

% Test data
test_saffron(Color, Size, Shape, Thickness) :-
    format('Testing saffron with Color: ~w, Size: ~w, Shape: ~w, Thickness: ~w~n', [Color, Size, Shape, Thickness]),
    classify_saffron(Color, Size, Shape, Thickness, Grade),
    format('Grade: ~w~n', [Grade]),
    nl.

% Example usage:
% Test with different saffron data
:- initialization((
    test_saffron(red, big, straight, thick),
    test_saffron(yellow, medium, curved, medium),
    test_saffron(white, small, broken, thin)
)).
