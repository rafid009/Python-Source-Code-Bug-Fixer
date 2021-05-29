import numpy as np 

def function(x):

	u3 = 9
	t2 = x
	paths = []
	try:
		if u3 >= 3:
			u3 = 1-t2
			u3 = u3+x
			u3 = u3-8
			paths.append(1)
		else:
			x = 0+2
			t2 = u3/t2
			u3 = u3+u3
			paths.append(2)
		if x > 1:
			u3 = 4/2
			paths.append(3)
		else:
			u3 = u3-4
			t2 = t2*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))