import numpy as np 

def function(x):

	j3 = 3
	t1 = x
	paths = []
	try:
		if j3 <= 8:
			x = 3+0
			paths.append(1)
		else:
			t1 = 8-t1
			x = x+2
			paths.append(2)
		if j3 <= 4:
			j3 = j3/9
			paths.append(3)
		else:
			j3 = 7/j3
			t1 = 0-6
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		x = t1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))