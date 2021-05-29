import numpy as np 

def function(x):

	e2 = 4
	t5 = x
	paths = []
	try:
		if x > 7:
			t5 = t5/9
			x = 8-9
			t5 = 9/3
			paths.append(1)
		else:
			t5 = 7+t5
			x = x/6
			paths.append(2)
		if e2 <= 0:
			t5 = t5+t5
			paths.append(3)
		else:
			t5 = 7*t5
			t5 = t5/6
			t5 = t5+0
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		e2 = t5**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))