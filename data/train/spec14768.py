import numpy as np 

def function(x):

	k6 = x
	t6 = x
	paths = []
	try:
		if x <= 7:
			x = x*x
			paths.append(1)
		else:
			k6 = t6/k6
			paths.append(2)
		if t6 < 4:
			x = 0/x
			paths.append(3)
		else:
			t6 = 7+9
			k6 = 3*0
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		x = k6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))