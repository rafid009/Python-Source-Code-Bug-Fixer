import numpy as np 

def function(x):

	l9 = x
	m7 = x
	paths = []
	try:
		if m7 <= 0:
			x = x*3
			x = l9*x
			x = 7/x
			paths.append(1)
		else:
			l9 = x*3
			x = 9/l9
			m7 = l9-8
			paths.append(2)
		if l9 <= 7:
			x = 6/m7
			x = 8*m7
			x = x/x
			paths.append(3)
		else:
			l9 = 9/l9
			x = x+2
			x = 2/6
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		l9 = l9**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))