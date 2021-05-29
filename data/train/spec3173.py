import numpy as np 

def function(x):

	q5 = 6
	t9 = x
	paths = []
	try:
		if q5 >= 3:
			x = 7/2
			x = x+5
			t9 = t9*q5
			paths.append(1)
		else:
			q5 = q5+q5
			paths.append(2)
		if q5 >= 7:
			t9 = t9*0
			t9 = t9-9
			paths.append(3)
		else:
			t9 = 1-t9
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		q5 = t9**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))