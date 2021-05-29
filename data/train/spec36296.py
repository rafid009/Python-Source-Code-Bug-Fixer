import numpy as np 

def function(x):

	v8 = x
	m2 = 6
	paths = []
	try:
		if v8 >= 4:
			v8 = v8/x
			x = x-8
			paths.append(1)
		else:
			v8 = 4/v8
			m2 = 7+7
			m2 = v8/m2
			paths.append(2)
		if x < 2:
			m2 = 3+x
			x = x*7
			paths.append(3)
		else:
			x = x+5
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		v8 = v8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))