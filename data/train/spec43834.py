import numpy as np 

def function(x):

	v1 = x
	m1 = x
	paths = []
	try:
		if m1 > 8:
			v1 = v1-5
			m1 = x*9
			x = 5*x
			paths.append(1)
		else:
			x = 6*x
			paths.append(2)
		if m1 > 9:
			x = x+9
			paths.append(3)
		else:
			m1 = m1+7
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		x = v1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))