import numpy as np 

def function(x):

	g2 = x
	l5 = 7
	paths = []
	try:
		if x >= 3:
			g2 = x*7
			paths.append(1)
		else:
			l5 = l5-x
			x = x+l5
			x = x+5
			paths.append(2)
		if l5 <= 7:
			l5 = 0/5
			l5 = 5-l5
			paths.append(3)
		else:
			g2 = g2+1
			x = g2+x
			x = 6*l5
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		l5 = g2**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))