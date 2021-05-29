import numpy as np 

def function(x):

	l5 = 4
	f7 = x
	paths = []
	try:
		if l5 <= 1:
			x = 2*9
			f7 = 2*f7
			paths.append(1)
		else:
			f7 = f7+6
			l5 = f7*l5
			paths.append(2)
		if x <= 5:
			x = 4/1
			x = x+3
			l5 = l5*5
			paths.append(3)
		else:
			x = x*0
			l5 = l5*3
			x = 0/7
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		l5 = l5**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))