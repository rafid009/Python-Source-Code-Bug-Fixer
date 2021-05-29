import numpy as np 

def function(x):

	m1 = x
	l5 = x
	paths = []
	try:
		if m1 < 6:
			x = x+x
			paths.append(1)
		else:
			m1 = 2-m1
			l5 = 1/l5
			paths.append(2)
		if l5 > 4:
			x = x*0
			l5 = l5/l5
			x = m1+m1
			paths.append(3)
		else:
			l5 = 0/l5
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		x = m1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))