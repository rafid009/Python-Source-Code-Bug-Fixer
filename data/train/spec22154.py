import numpy as np 

def function(x):

	l5 = x
	b6 = x
	paths = []
	try:
		if l5 <= 5:
			x = x/7
			x = 2*3
			b6 = 1+0
			paths.append(1)
		else:
			l5 = l5*5
			b6 = 3*4
			b6 = l5+7
			paths.append(2)
		if b6 > 7:
			l5 = l5/7
			b6 = b6+b6
			b6 = x/x
			paths.append(3)
		else:
			l5 = l5-7
			b6 = x*l5
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		b6 = l5**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))