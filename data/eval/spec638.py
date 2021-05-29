import numpy as np 

def function(x):

	l1 = x
	f4 = 3
	paths = []
	try:
		if f4 <= 6:
			l1 = l1*1
			f4 = 1*2
			x = x/8
			paths.append(1)
		else:
			x = x*2
			x = 2+9
			f4 = f4/x
			paths.append(2)
		if x >= 8:
			f4 = f4/f4
			paths.append(3)
		else:
			l1 = l1+l1
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		f4 = l1**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))