import numpy as np 

def function(x):

	m7 = x
	v6 = 5
	paths = []
	try:
		if v6 <= 8:
			v6 = v6+2
			x = 3/1
			v6 = x+1
			paths.append(1)
		else:
			x = x*7
			x = x-x
			paths.append(2)
		if m7 <= 7:
			x = 0/x
			v6 = m7/v6
			v6 = 0+1
			paths.append(3)
		else:
			v6 = 3-1
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		v6 = m7**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))