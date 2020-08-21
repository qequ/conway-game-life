black = 0
white = 7
delay = 1
b = {}


function init_board()
    for i = 1, 127 do 
        add(b, {})
    end
    for i = 1, 127 do 
        for j = 1, 127 do 
            b[i][j] = black
        end
    end
end

function amount_living_neighbours(x, y)
    local res = 0
    for i= -1, 1 do 
        for j = -1,1 do
            if i == 0 and j == 0 then goto continue end
            if x+i >= 0 and x+i <= 127 and y+j >= 0 and y+j <= 127 then
                if pget(x+i, y+i) == white then
                    res += 1
                end
            end
            ::continue::
        end
    end
    return res
end


function update_board()
    local new_board = {}

    for i = 1, 127 do 
        add(b, {})
        add(new_board, {})
    end
    for i = 1, 127 do 
        for j = 1, 127 do 
            new_board[i][j] = black
        end
    end

    for x = 1, 127 do 
        for y = 1, 127 do 
            n_neigh = amount_living_neighbours(x, y)

            if is_alive(x, y) then
                if n_neigh < 2 or n_neigh > 3 then
                    new_board[x][y] = black -- the pixel is death
                end
            else
                if n_neigh == 3 then
                    new_board[x][y] =  white-- the pixel reborns
                end
            end
        end
    end

    return new_board
end

--check if a pixel is white
function is_alive(x, y)
    return pget(x, y) == white 
end

function _init()
    init_board()
    b[50][50] = white
    b[51][50] = white
    b[52][50] = white

end

function _update()
    if delay == 0 then
    b = update_board()
    delay = 1
    else delay -= 1
    end
    
end



function _draw()
    cls()
    for i = 1, 127 do 
        for j = 1, 127 do 
            pset(i, j, b[i][j])
        end
    end
end


