import numpy as np 

def function(x):

	l9 = x
	t1 = x
	x = x
	paths = []
	try:
		if x >= 7:
			l9 = l9-t1
			paths.append(1)
		else:
			x = x+x
			l9 = 7/7
			l9 = 3+8
			paths.append(2)
		if l9 <= 9:
			l9 = 0+l9
			t1 = 4*0
			paths.append(3)
		else:
			x = x-x
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