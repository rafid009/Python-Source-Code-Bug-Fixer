import numpy as np 

def function(x):

	j2 = x
	l5 = 9
	paths = []
	try:
		if x <= 2:
			j2 = 7/x
			l5 = l5*l5
			j2 = j2*0
			paths.append(1)
		else:
			x = x/l5
			paths.append(2)
		if l5 <= 3:
			j2 = j2*j2
			x = x*7
			x = j2+9
			paths.append(3)
		else:
			l5 = l5/x
			x = 5/x
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