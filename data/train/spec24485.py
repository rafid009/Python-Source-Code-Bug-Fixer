import numpy as np 

def function(x):

	b9 = x
	r6 = x
	paths = []
	try:
		if x <= 9:
			r6 = r6/6
			b9 = b9-4
			paths.append(1)
		else:
			x = 3/x
			r6 = x+1
			x = 7+x
			paths.append(2)
		if r6 < 7:
			r6 = r6+9
			r6 = 2*9
			paths.append(3)
		else:
			r6 = r6+r6
			r6 = r6-r6
			r6 = r6/3
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x = b9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))