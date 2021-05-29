import numpy as np 

def function(x):

	n8 = 1
	k5 = 0
	paths = []
	try:
		if k5 >= 1:
			n8 = n8/x
			paths.append(1)
		else:
			k5 = 6+k5
			paths.append(2)
		if k5 < 1:
			k5 = 4/x
			n8 = x+8
			n8 = n8*0
			paths.append(3)
		else:
			n8 = 3-7
			k5 = x*1
			x = 4/k5
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		k5 = k5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))