import numpy as np 

def function(x):

	u3 = 9
	q5 = x
	paths = []
	try:
		if q5 < 2:
			x = x*x
			paths.append(1)
		else:
			u3 = q5*u3
			paths.append(2)
		if x < 4:
			q5 = 2+u3
			u3 = u3*5
			q5 = q5-6
			paths.append(3)
		else:
			u3 = 4+q5
			x = 8-5
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))