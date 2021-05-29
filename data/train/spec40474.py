import numpy as np 

def function(x):

	i3 = x
	m1 = 1
	paths = []
	try:
		if i3 > 9:
			i3 = 3*5
			x = m1+9
			paths.append(1)
		else:
			m1 = i3*7
			m1 = x*9
			x = x+0
			paths.append(2)
		if i3 <= 9:
			x = m1*4
			x = x+x
			paths.append(3)
		else:
			x = x+5
			m1 = 0+2
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		i3 = m1**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))