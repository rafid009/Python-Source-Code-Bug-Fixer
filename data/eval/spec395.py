import numpy as np 

def function(x):

	a2 = x
	t5 = x
	paths = []
	try:
		if x <= 3:
			t5 = x-a2
			a2 = t5/a2
			x = x+x
			paths.append(1)
		else:
			x = x+9
			x = 4+x
			x = x*t5
			paths.append(2)
		if t5 > 9:
			t5 = 9-1
			x = x+7
			paths.append(3)
		else:
			x = 4-x
			a2 = a2-a2
			a2 = 8+a2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))