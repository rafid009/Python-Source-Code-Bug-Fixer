import numpy as np 

def function(x):

	m5 = x
	i6 = x
	paths = []
	try:
		if m5 > 0:
			x = x+3
			x = 1*5
			x = 6+x
			paths.append(1)
		else:
			m5 = x/1
			x = m5*0
			i6 = 1+i6
			paths.append(2)
		if i6 >= 0:
			x = 2-1
			m5 = m5-2
			i6 = m5/4
			paths.append(3)
		else:
			m5 = m5/7
			x = x+2
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		i6 = m5**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))