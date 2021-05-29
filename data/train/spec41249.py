import numpy as np 

def function(x):

	l5 = 7
	j6 = x
	paths = []
	try:
		if l5 > 3:
			x = 2+6
			paths.append(1)
		else:
			x = x+x
			l5 = l5*9
			j6 = 3+j6
			paths.append(2)
		if x <= 4:
			x = x*1
			l5 = l5/x
			paths.append(3)
		else:
			j6 = 4-9
			l5 = x/9
			l5 = 0*l5
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		x = j6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))