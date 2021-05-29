import numpy as np 

def function(x):

	m8 = 1
	i3 = x
	paths = []
	try:
		if x <= 6:
			i3 = i3/2
			m8 = m8*9
			paths.append(1)
		else:
			i3 = 4/i3
			x = x-m8
			paths.append(2)
		if x < 9:
			i3 = i3/5
			i3 = 2-0
			paths.append(3)
		else:
			m8 = x/x
			i3 = i3-3
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		i3 = i3**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))