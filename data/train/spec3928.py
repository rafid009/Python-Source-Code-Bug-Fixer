import numpy as np 

def function(x):

	n1 = x
	v6 = 7
	x = x
	paths = []
	try:
		if n1 < 9:
			x = 9-x
			paths.append(1)
		else:
			x = x/1
			x = 9+x
			paths.append(2)
		if x < 6:
			n1 = 6-n1
			n1 = n1/9
			x = 0/4
			paths.append(3)
		else:
			v6 = 8*2
			v6 = n1+9
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		v6 = v6**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))