import numpy as np 

def function(x):

	a2 = 1
	v5 = x
	paths = []
	try:
		if v5 < 5:
			a2 = a2/7
			paths.append(1)
		else:
			v5 = v5+a2
			v5 = v5/9
			a2 = a2*8
			paths.append(2)
		if a2 <= 5:
			a2 = 6+a2
			x = v5-2
			a2 = a2*8
			paths.append(3)
		else:
			a2 = 8/3
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		v5 = v5**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))