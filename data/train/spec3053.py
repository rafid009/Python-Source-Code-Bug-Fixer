import numpy as np 

def function(x):

	f6 = 7
	l3 = 6
	paths = []
	try:
		if f6 <= 4:
			f6 = 1+x
			l3 = l3+5
			paths.append(1)
		else:
			x = x+l3
			paths.append(2)
		if x > 3:
			f6 = f6-7
			f6 = f6-l3
			paths.append(3)
		else:
			l3 = x/7
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		f6 = l3**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))