import numpy as np 

def function(x):

	u3 = x
	t3 = x
	paths = []
	try:
		if t3 > 4:
			u3 = u3+1
			x = x-x
			paths.append(1)
		else:
			u3 = t3/x
			u3 = u3-5
			paths.append(2)
		if t3 > 8:
			u3 = x-5
			u3 = 8+6
			paths.append(3)
		else:
			x = t3*5
			u3 = u3/t3
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		t3 = u3**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))