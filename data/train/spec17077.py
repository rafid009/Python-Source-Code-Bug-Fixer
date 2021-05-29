import numpy as np 

def function(x):

	a9 = x
	j5 = x
	paths = []
	try:
		if j5 < 0:
			a9 = 2-a9
			x = x*j5
			x = 1*j5
			paths.append(1)
		else:
			j5 = 8-a9
			j5 = j5/4
			paths.append(2)
		if j5 <= 9:
			a9 = 2-a9
			j5 = j5+0
			j5 = x+j5
			paths.append(3)
		else:
			x = 5+x
			x = x*2
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))