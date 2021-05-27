import numpy as np 

def function(x):

	i3 = x
	m3 = 9
	paths = []
	try:
		if m3 <= 5:
			m3 = 8+m3
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if i3 > 8:
			x = x*9
			m3 = i3+4
			paths.append(3)
		else:
			i3 = x*6
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