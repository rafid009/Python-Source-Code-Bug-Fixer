import numpy as np 

def function(x):

	a2 = x
	t9 = x
	paths = []
	try:
		if t9 >= 2:
			a2 = 2*a2
			t9 = 4-x
			paths.append(1)
		else:
			x = 0*5
			t9 = t9/3
			x = x/7
			paths.append(2)
		if x > 5:
			t9 = t9-5
			paths.append(3)
		else:
			t9 = 5*3
			a2 = t9/6
			x = 8+t9
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		t9 = t9**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))