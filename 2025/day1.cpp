#include <type_traits>
#include <stdio.h>

template<bool B, int I>
class Rotation {
public:
    static constexpr bool right = B;
    static constexpr int amount = I;
};

template<int dial_position, typename = void, typename...>
consteval int get_password_impl(int zero_count) {
    return zero_count;
}

template<typename Rotation>
consteval int update_dial_postion(int current_dial_position, Rotation rotation) {
    if constexpr (rotation.right) {
        return current_dial_position + rotation.amount;
    } else {
        return current_dial_position - rotation.amount;
    }
}

template<int dial_position, typename Rotation, typename... Rotations>
consteval int get_password_impl(int zero_count, Rotation current, Rotations... extra) {
    constexpr int new_dial_position = update_dial_postion(dial_position, current);
    if constexpr (new_dial_position % 100 == 0) {
        ++zero_count;
    }
    return get_password_impl<new_dial_position>(zero_count, extra...);
}

template<typename... Rotations>
consteval int get_password(Rotations... r) {
    return get_password_impl<50>(0, r...);
}

int main() {
    int zeros = get_password(
        // Rotation<true, 19>{}
#include "day1_data.h"
    );
    printf("zeros: %i\n", zeros);
    return 1;
}
