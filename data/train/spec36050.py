import numpy as np 

def function(x):

	v5 = x
	n1 = x
	paths = []
	try:
		if v5 < 8:
			v5 = 3+0
			x = 2*2
			n1 = 1*n1
			paths.append(1)
		else:
			x = x/9
			x = 5-x
			paths.append(2)
		if x > 1:
			v5 = 1*8
			v5 = 2-v5
			x = x+v5
			paths.append(3)
		else:
			x = x*8
			v5 = v5/4
			v5 = 6/1
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))