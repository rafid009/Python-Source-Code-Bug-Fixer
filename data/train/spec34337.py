import numpy as np 

def function(x):

	f1 = 1
	l6 = x
	paths = []
	try:
		if f1 > 1:
			f1 = f1*l6
			f1 = 6*l6
			l6 = 5-f1
			paths.append(1)
		else:
			f1 = 7+f1
			f1 = 8+x
			l6 = 3/f1
			paths.append(2)
		if x <= 4:
			f1 = f1+f1
			f1 = 3+5
			x = f1+x
			paths.append(3)
		else:
			f1 = 2+f1
			l6 = 5-l6
			f1 = 5-6
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		f1 = l6**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))