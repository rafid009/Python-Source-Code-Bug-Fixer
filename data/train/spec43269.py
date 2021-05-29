import numpy as np 

def function(x):

	m2 = 5
	v1 = x
	x = x
	paths = []
	try:
		if v1 >= 4:
			x = 6+m2
			paths.append(1)
		else:
			m2 = m2/m2
			x = x/9
			v1 = v1*6
			paths.append(2)
		if m2 >= 9:
			x = 1-4
			x = x*9
			paths.append(3)
		else:
			x = 6*x
			v1 = 1+x
			m2 = m2*x
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		v1 = m2**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))